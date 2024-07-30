from m1 import crew

n_iterations = 2
inputs = {"c_name": "ACPL"}

try:
    print("Training Started...")
    crew().crew().train(n_iterations= n_iterations, inputs=inputs)

except Exception as e:
    raise Exception(f"An error occurred while training the crew: {e}")