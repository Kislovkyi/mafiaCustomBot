from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import random

API_TOKEN = 'YOUR_BOT_TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class Player:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.role = None
        self.is_alive = True


class MafiaGame:
    def __init__(self):
        self.players = []
        self.game_started = False
        self.roles = ["Mafia", "Citizen", "Citizen", "Doctor", "Sheriff"]
        self.night_phase = False

    def add_player(self, user_id, name):
        if any(p.user_id == user_id for p in self.players):
            return False
        self.players.append(Player(user_id, name))
        return True

    def assign_roles(self):
        random.shuffle(self.roles)
        for player, role in zip(self.players, self.roles):
            player.role = role

    def get_player_list(self):
        return [p.name for p in self.players]

    def get_player_by_id(self, user_id):
        return next((p for p in self.players if p.user_id == user_id), None)

    def start_game(self):
        if len(self.players) < 4:
            return False
        self.assign_roles()
        self.game_started = True
        return True


game = MafiaGame()


@dp.message_handler(commands=['startgame'])
async def start_game(message: types.Message):
    if game.game_started:
        await message.reply("Игра уже идет!")
        return

    game.players.clear()
    game.game_started = False
    await message.reply("🎲 *Игра 'Мафия' началась!*\n\nВведите `/join`, чтобы присоединиться.", parse_mode="Markdown")


@dp.message_handler(commands=['join'])
async def join_game(message: types.Message):
    if game.game_started:
        await message.reply("Игра уже началась!")
        return

    user = message.from_user
    if game.add_player(user.id, user.full_name):
        await message.reply(f"✅ *{user.full_name}* присоединился к игре.", parse_mode="Markdown")
    else:
        await message.reply(f"⚠️ *{user.full_name}*, вы уже в игре!", parse_mode="Markdown")


@dp.message_handler(commands=['players'])
async def list_players(message: types.Message):
    if not game.players:
        await message.reply("❌ Нет зарегистрированных игроков.")
        return

    player_list = "\n".join([f"👤 {p.name}" for p in game.players])
    await message.reply(f"📃 *Список игроков:*\n{player_list}", parse_mode="Markdown")


@dp.message_handler(commands=['begin'])
async def begin_game(message: types.Message):
    if game.game_started:
        await message.reply("Игра уже идет!")
        return

    if not game.start_game():
        await message.reply("❌ Недостаточно игроков! Нужно минимум 4.")
        return

    await message.reply("🎭 *Роли распределены!*")

    for player in game.players:
        try:
            await bot.send_message(player.user_id, f"🔎 Ваша роль: {player.role}")
        except:
            pass  # На случай, если бот не может отправить сообщение

    await message.reply("🌙 *Наступает ночь...* Мафия выбирает жертву!")


@dp.message_handler(commands=['startnight'])
async def start_night(message: types.Message):
    if not game.game_started:
        await message.reply("Игра ещё не началась!")
        return

    game.night_phase = True
    keyboard = InlineKeyboardMarkup()
    for player in game.players:
        if player.is_alive:
            keyboard.add(InlineKeyboardButton(player.name, callback_data=f"kill_{player.user_id}"))

    await message.reply("🌙 *Наступила ночь!* Мафия, выберите жертву:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('kill_'))
async def mafia_kill(callback_query: types.CallbackQuery):
    if not game.night_phase:
        return

    user_id = int(callback_query.data.split('_')[1])
    victim = game.get_player_by_id(user_id)
    if victim and victim.is_alive:
        victim.is_alive = False
        await bot.send_message(callback_query.message.chat.id, f"☠️ *{victim.name} был убит ночью!*")
        game.night_phase = False

    await bot.answer_callback_query(callback_query.id)


@dp.message_handler(commands=['dayvote'])
async def start_day_vote(message: types.Message):
    if not game.game_started:
        await message.reply("Игра ещё не началась!")
        return

    keyboard = InlineKeyboardMarkup()
    for player in game.players:
        if player.is_alive:
            keyboard.add(InlineKeyboardButton(player.name, callback_data=f"vote_{player.user_id}"))

    await message.reply("🌞 *День начался!* Голосуем, кто мафия!", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data.startswith('vote_'))
async def process_vote(callback_query: types.CallbackQuery):
    user_id = int(callback_query.data.split('_')[1])
    voted_player = game.get_player_by_id(user_id)

    if voted_player and voted_player.is_alive:
        voted_player.is_alive = False
        await bot.send_message(callback_query.message.chat.id, f"⚖️ *{voted_player.name} был казнён!*")

    await bot.answer_callback_query(callback_query.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
