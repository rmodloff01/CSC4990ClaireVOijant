class User < ApplicationRecord

	has_many :audios, dependent: :destroy
	has_many :connections, dependent: :destroy
	has_many :lights, dependent: :destroy
	has_many :videos, dependent: :destroy

  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable

         attr_accessor :username


end
