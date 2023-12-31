import time
class TrainProgressBar:
    def __init__(self, total_epochs, total_batches, bar_length=20):
        self.total_epochs = total_epochs
        self.total_batches = total_batches
        self.bar_length = bar_length
    
    def step(self, step, epoch,loss,acc,start_time,printing=True):
        est_time = time.perf_counter() - start_time
        progress = (step / self.total_batches)
        arrow = '#' * int(round(progress * self.bar_length) - 1)
        spaces = '-' * (self.bar_length - len(arrow) - 1)
        if printing:
            print(f"\r| Epoch {epoch:>3} / {self.total_epochs}: [{arrow}{spaces}] {progress * 100:7.2f}% | Loss: {loss:.4f} | Acc: {acc*100:7.2f}% | ETA: {est_time * (self.total_batches - step):7.1f}s | ", end='')
class EvalProgressBar:
    def __init__(self,total_batches, bar_length=20):
        self.total_batches = total_batches
        self.bar_length = bar_length
    
    def step(self, step,start_time):
        est_time = time.perf_counter() - start_time
        progress = (step / self.total_batches)
        arrow = '#' * int(round(progress * self.bar_length) - 1)
        spaces = '-' * (self.bar_length - len(arrow) - 1)
        print(f"\r| Evaluating: [{arrow}{spaces}] {progress * 100:7.2f}% | ETA: {est_time * (self.total_batches - step):7.1f}s | ", end='')
        if step == self.total_batches:
            print("Done!")