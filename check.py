import tensorflow as tf
print("GPU Available:", tf.config.list_physical_devices('GPU'))




import numpy as np

# Dummy test data (replace this with your real test data)
X_test = np.random.rand(100, 40)  # Example shape (100 samples, 40 features)
y_test = np.random.randint(0, 2, (100, 1))  # Example binary labels (0 or 1)

# Save the files
np.save("X_test.npy", X_test)
np.save("y_test.npy", y_test)

print("✅ Test data saved successfully!")


