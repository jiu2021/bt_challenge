import torch
import torch.nn as nn

# 定义LSTM模型
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)

        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# # 设置超参数
# input_size = 2  # 输入特征维度为2
# hidden_size = 32
# num_layers = 2
# output_size = 2  # 输出时间步为100
# learning_rate = 0.001
# num_epochs = 1000

# # 创建模型实例
# model = LSTMModel(input_size, hidden_size, num_layers, output_size)
# criterion = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# # 训练模型
# for epoch in range(num_epochs):
#     # 假设每个输入序列包含5个时间步，每个时间步有两个特征维度
#     inputs = torch.Tensor([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0], [4.0, 8.0], [5.0, 10.0]]).unsqueeze(0)
#     targets = torch.Tensor([[i/5 for i in range(100)]]).unsqueeze(0)

#     # 前向传播
#     outputs = model(inputs)
#     loss = criterion(outputs, targets)

#     # 反向传播和优化
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

#     if (epoch+1) % 100 == 0:
#         print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# # 使用训练好的模型进行预测
# model.eval()
# with torch.no_grad():
#     test_input = torch.Tensor([[6.0, 12.0]]).unsqueeze(0)
#     predicted_output = model(test_input)
#     predicted_output = predicted_output.squeeze().tolist()
#     print(f'Predicted Output: {predicted_output}')