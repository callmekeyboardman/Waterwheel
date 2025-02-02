from abc import abstractmethod, ABC


class INsClient(ABC):

    # 读取数据
    @abstractmethod
    def read_data(self):
        pass
