class CommentsController < ApplicationController
   protect_from_forgery with: :null_session
   def create
      @comment = Comment.new(secureComment)
      if @comment.valid?
         @comment.save
         redirect_to messages_index_path
      else
         flash[:alert] = @comment.errors.full_messages
         redirect_to messages_index_path
      end
   end
end
