from domain.valobj.goldprice.GoldPriceChartData import GoldPriceChartData


def convert(return_data: GoldPriceChartData):
    sorted_list = sorted(return_data.get_usd(), key=lambda x: x.get_time_stamp())

    col_names = []
    value_list = []

    value = []
    for i in range(len(sorted_list)):
        usd_data = sorted_list[i]
        col_names.append(usd_data.get_time_name())
        value.append(usd_data.value)
    value_list.append(value)
    result = {
        'row_names': ["美元/盎司"],
        'col_names': col_names,
        'values': value_list
    }
    return result
