import asyncio
import shutil
import os
from aiogram import Bot, Dispatcher
from aiogram.types import FSInputFile, InputPaidMediaPhoto
from config import TOKEN, photo_cost, channel

async def send_media_to_usepictures():
    for path, _, files in os.walk("pictures"):
        if not files:
            raise FileNotFoundError("No files found in the 'pictures' directory.")

        filepath = os.path.join(path, files[0])
        try:
            shutil.move(filepath, "usepictures")  # Використовуємо shutil.move замість os.replace
        except FileExistsError:
            print(f"File {filepath} already exists.")
        except PermissionError:
            print(f"Permission denied while moving {filepath}. Ensure you have sufficient permissions.")
        except Exception as e:
            print(f"An error occurred: {e}")


async def send_message(bot):
    file = get_pictures()
    if file is None:
        print("No media found to send.")
        return

    try:
        await bot.send_paid_media(chat_id=channel, star_count=photo_cost, media=file)
        await send_media_to_usepictures()
    except Exception as e:
        print(f"Failed to send photo: {e}")

def get_pictures():
    try:
        for path, _, files in os.walk("pictures"):
            if not files:
                raise FileNotFoundError("No files found in the 'pictures' directory.")

            filepath = os.path.join(path, files[0])
            print(f"Found file: {filepath}")

            # Повертаємо об'єкт InputPaidMediaPhoto
            return [InputPaidMediaPhoto(media=FSInputFile(filepath))]

        raise FileNotFoundError("'pictures' directory does not contain any files.")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

async def send():
    async with Bot(token=TOKEN) as bot:
        await send_message(bot)

def run_bot():
    try:
        asyncio.run(send())
    except Exception as e:
        print(f"Error encountered: {e}")

if __name__ == "__main__":
    run_bot()
