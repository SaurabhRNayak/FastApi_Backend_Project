# 🌐 Blogging Site Backend APIs

This project is a **backend API** for a blogging site, built with **FastAPI** and **MongoDB Atlas**. The API provides endpoints to create, read, update, and delete blog posts and supports searching and filtering based on various criteria.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Features
- **CRUD Operations**: Create, read, update, and delete blog posts.
- **Search and Filtering**: Search blog posts by name or ID with case-insensitive support.
- **MongoDB Atlas Integration**: Utilizes MongoDB Atlas as the cloud-based database.
- **FastAPI**: A high-performance asynchronous web framework.
- **Efficient Querying**: MongoDB querying with regular expressions for flexible filtering.
- **Error Handling**: Robust error handling to ensure stable API responses.

## Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance) web framework for building APIs with Python.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - Cloud-hosted MongoDB service for storing blog data.
- [Uvicorn](https://www.uvicorn.org/) - ASGI server for running FastAPI apps.

## Prerequisites
Before you begin, ensure you have the following installed:
- **Python** (3.8 or higher)
- **MongoDB Atlas Account** - [Sign up here](https://www.mongodb.com/cloud/atlas)

## Getting Started
Follow these steps to get the backend up and running:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/blogging-site-backend.git
cd blogging-site-backend
```

### 2. Set up the virtual environment
```bash
# Install conda if not already installed
conda create --name blog-env python=3.8
conda activate blog-env
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the `config/` directory and add the following:

```bash
ATLAS_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
ATLAS_PASSWORD=<your-atlas-password>
```

### 5. Run the app
```bash
uvicorn main:app --reload
```

Your FastAPI backend will be running locally at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

| Method | Endpoint                  | Description                     | Payload           |
|--------|---------------------------|---------------------------------|-------------------|
| GET    | `/all/blogs`             | Fetch all blog posts            | N/A               |
| GET    | `/blogs/{id}`            | Fetch a blog by ID              | N/A               |
| POST   | `/create/blog`           | Create a new blog               | `{ title, content }` |
| PATCH  | `/update/{id}`           | Update an existing blog         | `{ title, content }` |
| DELETE | `/delete/{id}`           | Delete a blog by ID             | N/A               |

### Example: Create a New Blog
```bash
POST /create/blog
Content-Type: application/json

{
  "title": "My First Blog",
  "content": "This is the content of my first blog."
}
```

### Example: Search Blog by Name (Case-Insensitive)
```bash
GET /search?name=blog
```

## Environment Variables
Ensure the following environment variables are set:
- `ATLAS_URI`: MongoDB Atlas connection string
- `ATLAS_PASSWORD`: Password for MongoDB Atlas

## Project Structure
```bash
.
├── config/                  # Configuration files (.env, MongoDB config)
│   └── config.py            # Config loader for MongoDB connection
├── models/                  # Database models for blog posts
├── routes/                  # API route definitions
├── serializers/             # Data serialization and validation
├── main.py                  # Application entry point
├── README.md                # Project documentation
└── requirements.txt         # List of dependencies
```

## Contributing
We welcome contributions! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

Thank you for checking out the **Blogging Site Backend APIs**! If you have any questions, feel free to reach out. Happy coding! 🚀
