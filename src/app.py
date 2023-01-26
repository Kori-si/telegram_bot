from aiogram.utils import executor

import middlewares
from handlers import dp

if __name__ == '__main__':
    middlewares.setup(dp)
    executor.start_polling(dispatcher=dp)
