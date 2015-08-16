from getresults_identifier import AlphanumericIdentifier


class PatientIdentifier(AlphanumericIdentifier):

    identifier_type = 'patient'
    alpha_pattern = r'^[A-Z]{3}$'
    numeric_pattern = r'^[0-9]{8}$'
    seed = ['AAA', '00000000']
