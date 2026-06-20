import pickle

model_path = 'model/model.pkl'

def load_model(model_path: str):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model