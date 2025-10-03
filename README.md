# markdown-calendar-generator

# 📅 markdown-calendar-generator

A Python script to generate customizable calendars in Markdown format with support for multiple languages (**English**, **French**, **Arabic**, **Spanish**), ISO week numbers, and flexible week start options.

---

## 🌟 Introduction

`markdown-calendar-generator` helps you create beautiful, shareable calendars in Markdown format directly from your terminal. It’s perfect for project management, documentation, scheduling, and more! The script supports multiple languages, ISO week numbers, and lets you choose your preferred starting day of the week.

---

## 🚀 Features

- **Customizable Calendars**: Generate calendars for any month and year.
- **Multi-language Support**: English, French, Arabic, and Spanish.
- **ISO Week Numbers**: Optionally display ISO week numbers.
- **Flexible Week Start**: Choose Sunday or Monday as the first day of the week.
- **Markdown Output**: Get your calendar in ready-to-use Markdown format.

---

## 🛠️ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/markdown-calendar-generator.git
    cd markdown-calendar-generator
    ```

2. **Install requirements (if any):**
    - This script only uses Python standard libraries (`calendar`, `datetime`, `argparse`, `sys`), so no external packages are needed.

---

## 📈 Usage

Generate a calendar in Markdown for any month and year with customizable options.

```bash
python markdown.py --year 2024 --month 6 --lang en --isoweek --start_sun
```

### Command-Line Arguments

| Argument      | Description                                                | Default   | Example       |
|:--------------|:----------------------------------------------------------|:----------|:--------------|
| `--year`      | Year of the calendar                                      | Required  | `--year 2024` |
| `--month`     | Month of the calendar (1-12)                              | Required  | `--month 6`   |
| `--lang`      | Language: `en`, `fr`, `ar`, `es`                         | `en`      | `--lang fr`   |
| `--isoweek`   | Show ISO week numbers                                     | Off       | `--isoweek`   |
| `--start_sun` | Start week on Sunday (by default, weeks start on Monday)  | Off       | `--start_sun` |

### Example

Generate a French calendar for March 2025, with ISO week numbers, starting on Sunday:

```bash
python markdown.py --year 2025 --month 3 --lang fr --isoweek --start_sun
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, submit issues, or open pull requests.

1. Fork the project.
2. Create your feature branch (`git checkout -b my-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin my-feature`).
5. Open a pull request.

Please follow the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

**Happy calendaring!** 👋

## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/Imranch4/markdown-calendar-generator
