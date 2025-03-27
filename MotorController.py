class MotorController:
    def __init__(self, speed, direction):
        self.power_on = False  # 初始状态为关闭
        self.speed = speed  # 速度
        self.direction = direction  # 方向: forward, backward

    def set_speed(self, new_speed):
        self.speed = new_speed
        print("电机速度已更改为", self.speed)

    def get_speed(self):
        print("当前电机速度为", self.speed)

    def set_direction(self, new_direction):
        self.direction = new_direction
        print("电机方向已更改为", self.direction)

    def get_direction(self):
        print("当前电机方向为", self.direction)

    def power_on_off(self, state):
        self.power_on = state
        print("电机已打开" if state else "电机已关闭")


# 设置初始电机速度以及电机方向
speed = int(input("请输入初始的电机速度："))
direction = input("请输入初始的电机方向(forward/backward):")

# 创建电机控制器对象
motor = MotorController(speed, direction)

while True:
    d = int(input("\n请输入数字选择你的模式:\n"
                  "0. 关闭电机\n"
                  "1. 打开电机\n"
                  "2. 修改电机速度\n"
                  "3. 查看当前电机速度\n"
                  "4. 修改电机方向\n"
                  "5. 查看当前电机方向\n"
                  "请输入你的选择: "))

    if d == 0:
        motor.power_on_off(False)
        break
    elif d == 1:
        motor.power_on_off(True)
    elif d == 2:
        new_speed = int(input("请输入新的电机速度："))
        motor.set_speed(new_speed)
    elif d == 3:
        motor.get_speed()
    elif d == 4:
        new_direction = input("请输入新的电机方向(forward/backward): ")
        motor.set_direction(new_direction)
    elif d == 5:
        motor.get_direction()
    else:
        print("无效输入，请重新选择！")

