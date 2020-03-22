# @File  : get_log.py
# @Author: yize365
# @Date  :  2020/02/24
# @Function:
# @Remarks:
import logging.handlers
class Get_Log:
    logger=None
    @classmethod
    def get_log(cls,filename):
        if cls.logger is None:
            #获取日志器
            cls.logger = logging.getLogger()
            #设置日志器级别
            cls.logger.setLevel(logging.INFO)
            #获取处理器 控制台
            sh=logging.StreamHandler()
            #获取处理器 文件-以时间分割
            th=logging.handlers.TimedRotatingFileHandler(filename="../log/"+filename,
                                                         when="midnight",
                                                         interval=1,
                                                         backupCount=30,
                                                         encoding="utf-8")
            #设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s [%(funcName)s:%(lineno)d] - %(message)s"
            fm=logging.Formatter(fmt)

            #将格式器添加到 处理器 控制台
            sh.setFormatter(fm)
            #将格式器添加到 处理器 文件
            th.setFormatter(fm)
            #将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
            return cls.logger

"""
#举例:
if __name__ == '__main__':
    logger=Get_Log().get_log("log01.log")
    logger.info("info信息被执行")
    logger.error("error信息被执行")

#其他模块调用 使用单例
#导包
# log=Get_Log().get_log("文件名")
"""