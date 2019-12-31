class Comment < ApplicationRecord
  validates :comment, presence: true
  validates :comment, length: { minimum: 10 }

  belongs_to :user
  belongs_to :message
end
