import subprocess

def generate_short_story(prompt, checkpoint_file, temperature=0.9, steps=256, additional_flags=None):
    # Define the path to the C executable (since it's in the same directory, use ./run)
    c_executable = './run'
    
    # Encode the prompt into bytes for passing to the subprocess
    prompt_bytes = prompt.encode('utf-8')
    
    # Construct the command to run the C executable with the given arguments
    command = [
        c_executable,
        checkpoint_file,
        str(temperature),
        str(steps),
        prompt_bytes
    ]
    
    # If additional flags are provided, add them to the command
    if additional_flags:
        command.extend(additional_flags)
    
    # Run the C executable and capture its output
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        # Decode the output and return it
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        # If an error occurs during execution, print the error message and return None
        print(f"Error executing C script: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    checkpoint_file = 'path/to/your/model.bin'
    prompt_text = "Once upon a time, in a faraway land,"
    additional_flags = ['-max-len', '512']  # Example: Set max token length to 512
    short_story = generate_short_story(prompt_text, checkpoint_file, temperature=1.0, steps=512, additional_flags=additional_flags)
    print(short_story)
