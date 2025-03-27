class MotorController:
    def __init__(self):
        self.power_on = 0  # 电机状态
        self.speed = 0  # 速度
        self.direction = "stopped"  # 方向: forward, backward, stopped
    
    def power(self, state: bool):
        """开启或关闭电机"""
        self.power_on = state
        if state==1:
            print("电机已开启！")
        else:
            print("电机已关闭！")
        
    def set_speed(self, speed: int):
        """设置电机速度"""
        if self.power_on==0:
               print("请先开启电机！")
               return
        else :
            self.speed = speed
            print(f"速度设置为 {speed}")
    
    def set_direction(self, direction: str):
        """设置电机方向"""
        if self.power_on==0:
            print("请先开启电机！")
            return
        if direction in ["forward", "backward", "stopped"]:
            self.direction = direction
            print(f"方向设置为 {direction}")
        else:
            print("无效方向")
    
    def get_status(self):
        """获取电机状态"""
        return {
            "power_on": self.power_on,
            "speed": self.speed,
            "direction": self.direction
        }

# 运行控制器
def main():
    controller = MotorController()
    print("电机控制器初始化完成。")

    # 开启电机，设置模式、速度和方向
    controller.power(a)
    controller.set_speed(b)
    controller.set_direction(c)


    # 获取状态
    status = controller.get_status()
    print("当前状态:", status)
    
    # 关闭电机
    controller.power(False)
    print("程序结束。")

#对a,b,c进行定义
a=int(input("请输入电机状态(0/1):"))
b=input("请输入速度：")
c=input("请输入方向(forward/backward/stopped):")

if __name__ == "__main__":
    main()

