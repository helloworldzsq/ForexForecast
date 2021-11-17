

# 即一次训练所抓取的数据样本数量
batch_size = 32

window_size = int(256) # must be a multiple of batch_size
# 验证集大小  设为数据集的1%
validation_size = 162 * batch_size # must be a multiple of batch_size
# 测试集大小
test_size = 162 * batch_size # must be a multiple of batch_size

# 简单移动平均线周期长度
ma_periods = 14 # Simple Moving Average periods length
# 数据文件名
ticker = 'USDJPY.M1' # Your data file name without extention
# 开始日期
start_date = '2001-01-01' # Ignore any data in the file prior to this date
# 设定一个种子
seed = 42 # An arbitrary value to make sure your seed is the same

model_path = f'models/{ticker}-{batch_size}-{window_size}-{ma_periods}'
scaler_path = f'scalers/{ticker}-{batch_size}-{window_size}-{ma_periods}.bin'

full_time_series_path = f'data/{ticker}.csv'

train_time_series_path = f'data/{ticker}-train.csv'
validate_time_series_path = f'data/{ticker}-validate.csv'
test_time_series_path = f'data/{ticker}-test.csv'