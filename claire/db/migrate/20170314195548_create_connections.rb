class CreateConnections < ActiveRecord::Migration[5.0]
  def change
    create_table :connections do |t|
      t.string :user_id
      t.string :ip_address
      t.string :username
      t.string :password

      t.timestamps
    end
  end
end
