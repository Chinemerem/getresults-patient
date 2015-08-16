from getresults_identifier import AlphanumericIdentifier

from getresults.models import IdentifierHistory


class PatientIdentifier(AlphanumericIdentifier):

    identifier_type = 'patient'
    alpha_pattern = r'^[A-Z]{3}$'
    numeric_pattern = r'^[0-9]{8}$'
    seed = ['AAA', '00000000']
    history_model = IdentifierHistory
