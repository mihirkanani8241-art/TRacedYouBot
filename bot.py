from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to TRacedYouBot!\n\nCommands:\n/today\n/weeklyplan\n/resources"
    )

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Today's Study Plan:\n\nCL250 - 90 min\nEC101 - 60 min\nGP203 - 60 min"
    )

async def weeklyplan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Monday: CL250 + EC101\nTuesday: GP201 + GP203\nWednesday: GP205 + GP207\nThursday: CL250 + EC101\nFriday: GP201 + GP203\nSaturday: GP205 + GP207\nSunday: ES250 + HS250"
    )

async def resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "CL250: MIT OCW + LearnChemE\nEC101: OpenStax + Khan Academy\nGP203: MIT Seismology + USGS"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("today", today))
    app.add_handler(CommandHandler("weeklyplan", weeklyplan))
    app.add_handler(CommandHandler("resources", resources))

    app.run_polling()

if __name__ == "__main__":
    main()
