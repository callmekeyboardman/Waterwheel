from abc import abstractmethod, ABC


class ICpiClient(ABC):

    # 读取 cpi 数据，读取2021~当前的CPI数据
    @abstractmethod
    def read_cpi_data(self):
        pass
