class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  before_action :authorize, except: [:new, :create]
  private
  def current_user
    User.find_by(id: session[:user_id]) if session[:user_id]
  end
  def secureUser
    params.require(:user).permit(:name, :email, :password, :password_confirmation)
  end
  def secureMessage
    params.require(:messages).permit(:message).merge(user: current_user)
  end
  def secureComment
    message = Message.find_by(id: params[:id])
    params.require(:cmt).permit(:comment).merge(user: current_user, message: message)
  end
  def logged?
    !current_user.nil?
  end
  def authorize
    unless logged?
      redirect_to '/user/new'
    end
  end
end
