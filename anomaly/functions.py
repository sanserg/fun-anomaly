import logging
from sklearn import metrics
from iotfunctions import bif
from iotfunctions.ui import UIMultiItem, UISingle ,UISingleItem, UIFunctionOutSingle, UIFunctionOutMulti
from iotfunctions.base import BaseRegressor, BaseClassifier
from iotfunctions.bif import AlertHighValue


logger = logging.getLogger(__name__)

PACKAGE_URL = 'git+https://github.com/fe01134/fun-anomaly@'


_IS_PREINSTALLED = False

class AnomalyDetector(BaseRegressor):

    '''
    Sample function uses a regression model to predict the value of one or more output
    variables. It compares the actual value to the prediction and generates an alert
    when the difference between the actual and predicted value is outside of a threshold.
    '''
    #class variables
    train_if_no_model = True
    estimators_per_execution = 3
    num_rounds_per_estimator = 3

    def __init__(self, features, targets, threshold,
                 predictions=None, alerts = None):
        super().__init__(features=features, targets = targets, predictions=predictions)
        logging.debug('init features %s ' %features)
        logging.debug('init targets %s ' %targets)
        logging.debug('init predictions %s ' %predictions)
        logging.debug('init alerts %s ' %alerts)

        if alerts is None:
            alerts = ['%s_alert' %x for x in self.targets]
        self.alerts = alerts
        self.threshold = threshold
        logging.debug('init exiting alerts %s ' %alerts)
        logging.debug('init exiting threshold %s ' %threshold)

    def execute(self,df):

        df = super().execute(df)
        for i,t in enumerate(self.targets):
            prediction = self.predictions[i]
            logging.debug('execute individual prediction %s ' %prediction)
            logging.debug('execute df t %s ' %df[t])
            logging.debug('execute df prediction absolute %s ' %df[prediction] )

            df['_diff_'] = (df[t] - df[prediction]).abs()
            alert = AlertHighValue(input_item = '_diff_',
                                      upper_threshold = self.threshold,
                                      alert_name = self.alerts[i])
            alert.set_entity_type(self.get_entity_type())
            logging.debug('execute df diff %s ' %df['_diff_'])
            logging.debug('execute get entity type %s ' %self.get_entity_type() )
            df = alert.execute(df)
            logging.debug('execute returning df  ------')
            logging.debug( df.head() )
        return df

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(UIMultiItem(name='features',
                                  datatype=float,
                                  required=True
                                          ))
        inputs.append(UIMultiItem(name='targets',
                                  datatype=float,
                                  required=True,
                                  output_item='predictions',
                                  is_output_datatype_derived=True
                                          ))
        inputs.append(UISingle(name='threshold',
                               datatype=float,
                               description=('Threshold for firing an alert. '
                                            'Expressed as absolute value not percent.')))
        #define arguments that behave as function outputs
        outputs = []
        outputs.append(UIFunctionOutMulti(name = 'alerts',
                                          datatype = bool,
                                          cardinality_from = 'targets',
                                          is_datatype_derived = False,
                                          ))

        return (inputs,outputs)

class SimpleRegressor(BaseRegressor):

    '''
    Sample function that predicts the value of a continuous target variable using the selected list of features.
    This function is intended to demonstrate the basic workflow of training, evaluating, deploying
    using a model.
    '''
    #class variables
    train_if_no_model = True
    estimators_per_execution = 3
    num_rounds_per_estimator = 3

    def __init__(self, features, targets, predictions=None):
        super().__init__(features=features, targets=targets, predictions=predictions)

    @classmethod
    def build_ui(cls):
        # define arguments that behave as function inputs
        inputs = []
        inputs.append(UIMultiItem(name='features',
                                  datatype=float,
                                  required=True
                                  ))
        inputs.append(UIMultiItem(name='targets',
                                  datatype=float,
                                  required=True,
                                  output_item='predictions',
                                  is_output_datatype_derived=True
                                  ))
        return (inputs,[])

class SimpleClassifier(BaseClassifier):

    '''
    Sample function that predicts the value of a discrete target variable using the selected list of features.
    This function is intended to demonstrate the basic workflow of training, evaluating, deploying
    using a model.
    '''

    eval_metric = staticmethod(metrics.accuracy_score)
    #class variables
    train_if_no_model = True
    estimators_per_execution = 3
    num_rounds_per_estimator = 3

    def __init__(self, features, targets, predictions=None):
        super().__init__(features=features, targets = targets, predictions=predictions)

    @classmethod
    def build_ui(cls):
        # define arguments that behave as function inputs
        inputs = []
        inputs.append(UIMultiItem(name='features',
                                  datatype=float,
                                  required=True
                                  ))
        inputs.append(UIMultiItem(name='targets',
                                  datatype=float,
                                  required=True,
                                  output_item='predictions',
                                  is_output_datatype_derived=True
                                  ))
        return (inputs,[])

class SimpleBinaryClassifier(BaseClassifier):

    '''
    Sample function that predicts the value of a discrete target variable using the selected list of features.
    This function is intended to demonstrate the basic workflow of training, evaluating, deploying
    using a model.
    '''

    eval_metric = staticmethod(metrics.f1_score)
    #class variables
    train_if_no_model = True
    estimators_per_execution = 3
    num_rounds_per_estimator = 3

    def __init__(self, features, targets, predictions=None):
        super().__init__(features=features, targets = targets, predictions=predictions)
        for t in self.targets:
            self.add_training_expression(t, 'df[%s]=df[%s].astype(bool)' %(t,t))

    @classmethod
    def build_ui(cls):
        # define arguments that behave as function inputs
        inputs = []
        inputs.append(UIMultiItem(name='features',
                                  datatype=float,
                                  required=True
                                  ))
        inputs.append(UIMultiItem(name='targets',
                                  datatype=float,
                                  required=True,
                                  output_item='predictions',
                                  is_output_datatype_derived=True
                                  ))
        return (inputs,[])
