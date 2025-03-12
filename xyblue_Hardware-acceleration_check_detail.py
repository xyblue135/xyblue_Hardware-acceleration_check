import subprocess

# Function to get the list of supported hardware acceleration methods
def get_supported_hwaccels():
    try:
        # Run the ffmpeg command to get the list of supported hardware accelerations
        result = subprocess.run(
            ['ffmpeg', '-hwaccels'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the command was successful and extract supported hwaccels
        if result.returncode == 0:
            hwaccels = result.stdout.splitlines()
            return [hwaccel.strip() for hwaccel in hwaccels if hwaccel]
        else:
            print(f"Error getting hardware accelerations: {result.stderr}")
            return []
    except Exception as e:
        print(f"An error occurred while getting supported hwaccels: {e}")
        return []

# Function to check if the hardware acceleration methods are working
def check_hwaccels():
    supported_hwaccels = get_supported_hwaccels()
    
    # If there are no supported hwaccels, return
    if not supported_hwaccels:
        print("No hardware accelerations supported.")
        return

    # Test each supported hardware acceleration method
    for hwaccel in supported_hwaccels:
        try:
            # Run the ffmpeg command to test the hardware acceleration
            result = subprocess.run(
                ['ffmpeg', '-hwaccel', hwaccel, '-i', 'test_video.mp4', '-f', 'null', '-'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Check if the command was successful by looking at the stderr for error messages
            if result.returncode == 0:
                print(f"{hwaccel} hardware acceleration is supported and working.")
            else:
                print(f"{hwaccel} hardware acceleration failed.")
                print(f"Error: {result.stderr}")
        except Exception as e:
            print(f"An error occurred while testing {hwaccel}: {e}")

# Run the check
check_hwaccels()