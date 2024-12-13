# GitHub Activity CLI

A simple command-line application to fetch and display the recent activity of a GitHub user using the GitHub API. The application supports caching to minimize redundant API calls and allows filtering of activity by event type.

---

## Features

- Fetch recent activity of a GitHub user.
- Caching mechanism to avoid redundant API calls (5-minute cache).
- Filter activity by event type (e.g., `PushEvent`, `IssuesEvent`).
- Graceful handling of errors and invalid inputs.

---

## Requirements

- Python 3.x

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/github-activity-cli.git
   ```

2. Navigate to the project directory:
   ```bash
   cd github-activity-cli
   ```

3. Ensure you have Python 3.x installed on your system.

---

## Usage

Run the application from the command line:

### Fetch Recent Activity

```bash
python github_activity.py <username>
```

Example:
```bash
python github_activity.py Akumbom-Wesley
```

### Fetch Activity by Event Type

You can filter the activity by event type using the `--type` option:

```bash
python github_activity.py <username> --type <event_type>
```

Example:
```bash
python github_activity.py Akumbom-Wesley --type PushEvent
```

Supported event types include (but are not limited to):
- `PushEvent`
- `IssuesEvent`

---

## Caching

The application caches the user activity in a file named `activity_cache.json` to minimize redundant API requests. The cache is valid for 5 minutes. After this period, the application will fetch fresh data from the GitHub API.

---

## Error Handling

- If the username is invalid or the API request fails, an error message will be displayed.
- If no activity is found for the user, the application will notify the user.

---

## Example Output

### Recent Activity
```bash
Recent Activity:
- Pushed 2 commits to Akumbom-Wesley/some-repo
  Commit: Fix README formatting
  Commit: Update contributing guidelines
- Opened an issue in Akumbom-Wesley/another-repo: Add dark mode support
```

### Using Cached Data
```bash
Using cached data...
Recent Activity:
- Pushed 1 commit to Akumbom-Wesley/project-repo
  Commit: Initial project setup
```

### Filtering by Event Type
```bash
python github_activity.py Akumbom-Wesley --type PushEvent

Recent Activity:
- Pushed 3 commits to Akumbom-Wesley/sample-repo
  Commit: Add unit tests
  Commit: Refactor code
  Commit: Fix bugs
```

---

## Project Structure

- `github_activity.py`: Main script for fetching and displaying GitHub activity.
- `activity_cache.json`: Cache file for storing user activity (created at runtime).

---

## Contribution

1. Fork the repository.
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

