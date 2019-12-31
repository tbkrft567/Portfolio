class UserController < ApplicationController
   def new
      @logged = logged?
   end
   def create
      @user = User.new(secureUser)
      if @user.valid?
         @user.save
         redirect_to user_new_path
      else
         flash[:alert] = @user.errors.full_messages
         redirect_to user_new_path
      end
   end
end
