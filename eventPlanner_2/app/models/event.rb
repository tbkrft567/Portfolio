class Event < ApplicationRecord
  validates :name,  :date, :location, :state, presence: true
  belongs_to :user

  has_many :comments
  has_many :users_commented, through: :comments, source: :user
  has_many :RSVPs
  has_many :users_RSVPd, through: :RSVPs, source: :user
end
