FROM sanluosizhou/selfdl:latest
RUN pip install gym_unity mlagents==0.25.1
RUN cd /workspace && git clone https://github.com/bluebread/FooCar.git && cd FooCar && pip install -e .
