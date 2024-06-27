# 🌟 Auction Project

Welcome to the Auction Project, an online auction platform built with FastAPI and SQLAlchemy. This project provides a robust and scalable solution for managing auctions, users, bids, and photos, ensuring a seamless auction experience.

## ✨ Features

- **User Registration and Authentication**: Secure registration and login for users.
- **Auction Management**: Create, update, delete, and view auctions.
- **Bid Management**: Place, update, and view bids on auction items.
- **Photo Management**: Upload, retrieve, and delete photos for auction items.

## 🛠 Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: The SQL toolkit and Object-Relational Mapping (ORM) library for the database.
- **SQLite**: A lightweight, disk-based database used for development and testing.
- **Alembic**: A database migration tool for SQLAlchemy.
- **Uvicorn**: ASGI server for serving FastAPI applications.

## 🚀 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Fayoz05/Auction_fastapi.git
   cd Auction_fastapi

2. **Install the dependencies:**:

   ```bash
   pip install -r requirements.txt

3. **Set up the database:**:

   ```bash
   alembic upgrade head

4. **Run the application:**:

   ```bash
   uvicorn main:app --reload

### 🌐 Access the application:
Open your web browser and go to given link.

## 📂 Project Structure

- `main.py`: Entry point of the application.
- `models.py`: SQLAlchemy models for database schema.
- `routers_api`: Route definitions for different parts of the application (users, auctions, bids, photos).
- `auctionservice.py`: Contains logic related to managing auctions, including creation, modification, and deletion.
- `bidservice.py`: Manages bid-related operations such as placing bids, updating bids, and retrieving bid information.
- `photoservice.py`: Handles tasks related to managing photos associated with auctions, including uploading, retrieving, and deleting photos.
- `userservice.py`: Deals with user-related functionalities like user registration, login, profile updates, and user deletion.


## 🚪 API Endpoints

### User Endpoints
- **GET** `/api/user`: Get User by ID
- **GET** `/api/all_users`: Get All Users
- **POST** `/api/registration`: Register User
- **POST** `/api/login`: Login User
- **PUT** `/api/change_email`: Change User Email
- **PUT** `/api/change_password`: Change User Password
- **DELETE** `/api/delete_user`: Delete User

### Auction Endpoints
- **GET** `/all_auctions`: Get All Auctions
- **GET** `/get_exact_item`: Get Auction by ID
- **POST** `/create_auction`: Create Auction
- **PUT** `/change_name`: Change Auction Name
- **PUT** `/change_description`: Change Auction Description
- **PUT** `/change_starting_bid`: Change Starting Bid
- **PUT** `/change_end_time`: Change Auction End Time
- **PUT** `/extend_end_time`: Extend Auction End Time
- **PUT** `/finish_auction`: Finish Auction
- **DELETE** `/delete_auction`: Delete Auction
- **DELETE** `/delete_finished_auctions`: Delete Finished Auctions

### Photo Endpoints
- **GET** `/get_all_photos`: Get All Photos
- **POST** `/add_photo`: Add Photo
- **DELETE** `/delete_photo`: Delete Photo

### Bid Endpoints
- **GET** `/get_all_bids`: Get All Bids
- **GET** `/top5_bids_of_item`: Get Top 5 Bids of an Item
- **POST** `/make_bid`: Make a Bid
- **PUT** `/greater_bid`: Increase Bid Amount
- **PUT** `/lower_bid`: Decrease Bid Amount
- **DELETE** `/delete_bid`: Delete Bid
- **DELETE** `/delete_user_bids`: Delete User Bids

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

## 🤝 Contributing
Contributions are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute to this project.

## 🙌 Acknowledgements
Special thanks to the FastAPI, SQLAlchemy, and Alembic communities for their excellent tools and documentation.

   ```css
  This format uses markdown syntax to structure headings, lists, code blocks, and inline code, suitable for a standard README.md file. Adjust the paths, URLs,
