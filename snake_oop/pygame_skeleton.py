import pygame
import time
import random


class App:
    # 定義靜態的常數
    # 例如顔色等

    def __init__(self):
        # 建構子
        # 游戲中可調整的狀態變數做爲物件屬性
        self.running = True
        pass

    def on_init(self):
        # 第一次初始化游戲狀態時呼叫
        pass

    def on_restart(self):
        # 游戲重新開始時呼叫
        pass

    def on_event(self, event):
        # 當觸發某事件時呼叫
        pass

    def on_loop(self):
        # 主要loop 中每個循環呼叫一次, 主要用來更新游戲狀態值
        pass

    def on_render(self):
        # 主要loop 中每個循環呼叫一次, 主要用來更新游戲畫面
        pass

    def on_cleanup(self):
        # 游戲結束時呼叫, 釋放資源
        pass

    def on_execute(self):
        # 主要架構方法
        self.on_init()
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    # 其他方法


# 主要方法
def main():
    theApp = App()
    theApp.on_execute()


if __name__ == '__main__':
    main()
