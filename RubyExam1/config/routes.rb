Rails.application.routes.draw do
  get '/', to: 'users#new'

  post 'members/create/:id', to: 'members#create'
  post 'members/create'
  

  delete 'members/destroy'

  post 'groups/create'

  delete 'groups/destroy'

  get 'groups/show'

  get 'groups/index'

  post 'sessions/create'

  delete 'sessions/destroy'

  get 'users/new'

  post 'users/create'

  match '*path' => redirect('/users/new'), via: :get
  match '*path' => redirect('/sessions/destroy'), via: :post
  match '*path' => redirect('/sessions/destroy'), via: :delete
end
