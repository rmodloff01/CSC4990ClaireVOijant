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

  get 'getpic' => 'pages#getpic'

  get 'getvid' => 'pages#getvid'

  get 'recsound' => 'pages#recsound'

  get 'livestream' => 'pages#livestream'

  get 'randsound' => 'pages#randsound'

  get 'stopsound' => 'pages#stopsound'

  get 'gallery' => 'pages#gallery'

  get 'sendit' => 'pages#sendit'

end
