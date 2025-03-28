import gradio as gr
import numpy as np
import pickle

# Dummy Perceptron Model (Replace with trained model)
def perceptron_model(features):
    weights = np.array([0.2, 0.3, 0.1, 0.2, 0.3, 0.4, 0.5])  # Example weights
    bias = -1.5  # Example bias
    score = np.dot(features, weights) + bias
    return "Employable" if score >= 0 else "Less Employable"

# Function to evaluate user input
def evaluate_employment(name, *ratings):
    features = np.array(ratings, dtype=float)
    result = perceptron_model(features)
    if result == "Employable":
        return f"Congrats {name}!!! 🎉 You are employable."
    else:
        return f"Try to upgrade yourself, {name}! 📚 Keep improving."

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## Employment Capability Assessment")
    name = gr.Textbox(label="Enter your Name")
    sliders = [gr.Slider(1, 5, step=1, label=col) for col in [
        "General Appearance", "Manner of Speaking", "Physical Condition", 
        "Mental Alertness", "Self-Confidence", "Ability to Present Ideas", 
        "Communication Skills"]]
    evaluate_button = gr.Button("Get Yourself Evaluated")
    output = gr.Textbox()
    
    evaluate_button.click(evaluate_employment, inputs=[name] + sliders, outputs=output)

demo.launch()
