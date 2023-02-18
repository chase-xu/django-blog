# base image  
FROM python:3.8   
# setup environment variable  
ENV HOME=/home/app

# set work directory  
RUN mkdir -p $HOME  

# where your code lives  
WORKDIR $HOME  

# set environment variables  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $HOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver  

# WORKDIR /app
# COPY package*.json ./ 
# RUN echo "running npm install ..."
# RUN npm ci --omit=dev
# RUN echo "Finished npm install"

# COPY . ./
# RUN echo "running run build ..."
# RUN npm run build
# RUN echo "Finished run build ..."
# RUN echo "running npm start"
# RUN echo "Finished running npm start"
# CMD ["npm", "start"]

# EXPOSE $PORT
