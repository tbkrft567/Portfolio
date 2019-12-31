class UsersController < ApplicationController
  def create
    @user = User.new(secureUser)
    if @user.valid?
      @user.save
      session[:user_id] = @user.id
      redirect_to  groups_index_path
    else
      flash[:alert] = @user.errors.full_messages
      redirect_to users_new_path
      end
  end

  def new
    # @logged = logged?
  end

end
