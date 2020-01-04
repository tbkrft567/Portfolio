Rails.application.routes.draw do
  get '/', to: 'user#new'
  get '/user/new', to: 'user#new'
  post '/user/create', to: 'user#create'
  post '/sessions/create', to: 'sessions#create'
  delete '/sessions/destroy', to: 'sessions#destroy' 
  get '/messages/index', to: 'messages#index'
  post '/messages/create', to: 'messages#create'
  delete '/messages/destroy', to: 'messages#destroy'
  delete '/comments/destroy', to: 'comments#destroy'
  post '/comments/create', to: 'comments#create'
  match '*path' => redirect('/user/new'), via: :get
end
