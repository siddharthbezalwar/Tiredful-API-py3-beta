# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# This file is part of Tiredful API application

from rest_framework import serializers

from advertisements.models import Classified


# Classfied object serializer
class ClassifiedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classified
        fields = ('headline', 'info', 'price', 'user')
