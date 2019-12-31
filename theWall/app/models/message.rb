class Message < ApplicationRecord
  validates :message, presence: true
  belongs_to :user
  has_many :comments, dependent: :destroy
end
