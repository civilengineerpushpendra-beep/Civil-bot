import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Namaste! 👷 Mai Civil Engineering Bot hu.\n\n"
        "Commands:\n"
        "/bbs - Bar Bending Schedule\n"
        "/bill - Billing Format\n"
        "/boq - BOQ Format\n"
        "/estimate - Estimate nikalo\n\n"
        "Koi bhi sawal pucho jaise: 1m3 concrete me cement kitna?"
    )

async def help_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    # Simple Civil Answers
    if "cement" in text and "1m3" in text or "1 m3" in text:
        reply = "1m3 M25 Concrete me:\nCement: 11 bag\nSand: 0.44 m3\nAggregate: 0.88 m3\nWater: 180 Litre"
    elif "bbs" in text:
        reply = "BBS Formula: Cutting Length = Total Length - 2*cover + 2*10d\nHook = 9d\nTum length bhejo mai BBS bana dunga."
    elif "bill" in text:
        reply = "Billing Format:\nS.No | Item | Qty | Rate | Amount\nBOQ se qty lo, Rate se multiply karo."
    elif "boq" in text:
        reply = "BOQ me kya chahiye?\n1. Earthwork\n2. PCC\n3. RCC\n4. Brickwork\n5. Plaster\nItem batao."
    else:
        reply = f"Tumne pucha: {text}\n\nMai iska civil engineering se jawab dunga. Thoda detail me pucho jaise 'slab ka steel kaise nikalte hai'"

    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, help_bot))
    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
