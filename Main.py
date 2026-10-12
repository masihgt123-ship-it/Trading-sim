from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

PRICES = [
    100, 101, 103, 102, 104, 106, 105, 107, 109, 108,
    110, 112, 111, 109, 107, 106, 104, 103, 105, 107,
    106, 104, 102, 100, 98, 97, 99, 101, 100, 98,
    96, 95, 97, 99, 101, 103, 102, 104, 106, 105,
    103, 101, 100, 102, 104, 103, 101, 99, 98, 100,
]

WINDOW = 5
START_CASH = 1000.0


def run_sim():
    cash = START_CASH
    coins = 0.0
    buys = 0
    sells = 0

    for i in range(WINDOW, len(PRICES)):
        price = PRICES[i]
        avg = sum(PRICES[i - WINDOW:i]) / WINDOW

        if price > avg and coins == 0:
            coins = cash / price
            cash = 0.0
            buys += 1
        elif price < avg and coins > 0:
            cash = coins * price
            coins = 0.0
            sells += 1

    if coins > 0:
        cash = coins * PRICES[-1]
        sells += 1

    profit = cash - START_CASH
    return (
        f"شروع: {START_CASH:.2f}\n"
        f"پایان: {cash:.2f}\n"
        f"سود یا ضرر: {profit:.2f}\n"
        f"معامله‌ها: {buys + sells}"
    )


class TradeSim(App):
    def build(self):
        box = BoxLayout(orientation="vertical", padding=24, spacing=16)
        self.result = Label(
            text="دکمه را بزن تا شبیه‌سازی اجرا شود.\nاین برنامه معامله واقعی نمی‌کند.",
            font_size="20sp",
        )
        button = Button(text="اجرا", size_hint_y=0.25, font_size="22sp")
        button.bind(on_press=self.show_result)
        box.add_widget(self.result)
        box.add_widget(button)
        return box

    def show_result(self, _button):
        self.result.text = run_sim()


if __name__ == "__main__":
    TradeSim().run()
