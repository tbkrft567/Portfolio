Rails.application.routes.draw do
  post 'comments/create'

  post 'events/create'

  get 'events/edit'

  patch 'events/update'

  delete 'events/destroy'

  get 'events/show'

  get 'events/index'

  post 'sessions/create'

  delete 'sessions/destroy'

  get 'users/new'

  post 'users/create'

  get 'users/edit'

  post 'users/update'

  delete 'users/destroy'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
