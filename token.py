from github import Github

# Enter your GitHub personal access token
ACCESS_TOKEN = "your-access-token"

# Enter the repository details
REPO_OWNER = "your-username"
REPO_NAME = "your-repository-name"

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def upload_to_github(file_content, file_name):
    g = Github(ACCESS_TOKEN)
    repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)
    contents = repo.get_contents("")
    repo.create_file(f"{file_name}", "Adding Fibonacci sequence", file_content, branch="main")
    print(f"Uploaded {file_name} to GitHub!")

def main():
    n = int(input("Enter the number of terms: "))
    fibonacci_sequence = generate_fibonacci_sequence(n)
    file_content = "\n".join(str(num) for num in fibonacci_sequence)
    file_name = f"fibonacci_{n}_terms.txt"
    upload_to_github(file_content, file_name)

if __name__ == "__main__":
    main()
