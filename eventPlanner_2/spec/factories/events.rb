FactoryBot.define do
  factory :event do
    name { "" }
    date { "2019-12-15" }
    location { "MyString" }
    state { "MyString" }
    user { nil }
  end
end
