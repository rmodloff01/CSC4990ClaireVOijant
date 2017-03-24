Rails.application.routes.draw do
  resources :videos
  resources :lights
  resources :connections
  resources :audios
  devise_for :admins
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  root :to => 'pages#home'

  get 'welcome' => 'pages#home'

end
