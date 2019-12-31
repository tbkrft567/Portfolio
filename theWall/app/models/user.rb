class User < ApplicationRecord
  has_secure_password

  has_many :messages
  has_many :comments
  has_many :messages_commented, through: :comments, source: :message
end
