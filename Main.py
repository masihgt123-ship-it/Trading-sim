from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import random


class TradeSim(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=16, spacing=10, **kwargs)

        self.cash = 10000.0
        self.btc = 0.0
        self.price = 60000.0
        self.lines = ["شبیه‌ساز آموزشی. پول واقعی نیست."]

        self.status = Label(text="", font_size="20sp", size_hint_y=None, height="140dp")
        self.log = Label(text="", font_size="16sp", size_hint_y=None, halign="right", valign="top")
        self.log.bind(texture_size=self._fit_log)

        scroll = ScrollView()
        scroll.add_widget(self.log)

        buy = Button(text="خرید ۰.۰۱ بیت‌کوین", size_hint_y=None, height="56dp")
        sell = Button(text="فروش ۰.۰۱ بیت‌کوین", size_hint_y=None, height="56dp")
        buy.bind(on_press=self.buy)
        sell.bind(on_press=self.sell)

        self.add_widget(self.status)
        self.add_widget(buy)
        self.add_widget(sell)
        self.add_widget(scroll)

        self.refresh()
        Clock.schedule_interval(self.move_price, 1.5)

    def _fit_log(self, *_):
        self.log.height = self.log.texture_size[1]
        self.log.text_size = (self.width - 32, None)

    def refresh(self):
        worth = self.cash + self.btc * self.price
        self.status.text = (
            f"قیمت ساختگی: {self.price:,.0f} دلار\n"
            f"نقد: {self.cash:,.2f} دلار\n"
            f"بیت‌کوین: {self.btc:.4f}\n"
            f"ارزش کل: {worth:,.2f} دلار"
        )
        self.log.text = "\n".join(self.lines[-12:])

    def move_price(self, _dt):
        change = random.uniform(-0.004, 0.004)
        self.price = max(1000.0, self.price * (1 + change))
        self.refresh()

    def buy(self, _btn):
        amount = 0.01
        cost = amount * self.price
        if self.cash < cost:
            self.lines.append("نقد کافی نیست.")
        else:
            self.cash -= cost
            self.btc += amount
            self.lines.append(f"خرید {amount} با قیمت {self.price:,.0f}")
        self.refresh()

    def sell(self, _btn):
        amount = 0.01
        if self.btc < amount:
            self.lines.append("بیت‌کوین کافی نیست.")
        else:
            self.btc -= amount
            self.cash += amount * self.price
            self.lines.append(f"فروش {amount} با قیمت {self.price:,.0f}")
        self.refresh()


class TradeSimApp(App):
    def build(self):
        self.title = "Trade Sim"
        return TradeSim()


if __name__ == "__main__":
    TradeSimApp().run()
