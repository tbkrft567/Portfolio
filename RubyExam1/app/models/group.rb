class Group < ApplicationRecord
  validates :name, :description, presence: true
  validates :name, length: { minimum: 6 }
  validates :description, length: { minimum: 11 }
  belongs_to :user

  has_many :members, dependent: :destroy
  has_many :user_members, through: :members, source: :user
end
