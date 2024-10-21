import re

class StringRepresentation:
    def __init__(self, obj):
        self.attributes = {#'id': None,
            'id': None, 'related_id': None, 'class': None, 'type/scale': None, 'name': None, 'relevance': None,
            'text': None, 'help': None, 'language': None, 'validation': None, 'mandatory': None, 'encrypted': None,
            'other': None, 'default': None, 'same_default': None, 'allowed_filetypes': None, 'alphasort': None,
            'answer_order': None, 'answer_width': None, 'answer_width_bycolumn': None, 'array_filter': None,
            'array_filter_exclude': None, 'array_filter_style': None, 'assessment_value': None, 'category_separator': None,
            'choice_input_columns': None, 'choice_title': None, 'commented_checkbox': None, 'commented_checkbox_auto': None,
            'cssclass': None, 'date_format': None, 'date_max': None, 'date_min': None, 'display_columns': None,
            'display_rows': None, 'display_type': None, 'dropdown_dates': None, 'dropdown_dates_minute_step': None,
            'dropdown_dates_month_style': None, 'dropdown_prefix': None, 'dropdown_prepostfix': None, 'dropdown_separators': None,
            'dropdown_size': None, 'dualscale_headerA': None, 'dualscale_headerB': None, 'em_validation_q': None,
            'em_validation_q_tip': None, 'em_validation_sq': None, 'em_validation_sq_tip': None, 'equals_num_value': None,
            'equation': None, 'exclude_all_others': None, 'exclude_all_others_auto': None, 'hidden': None, 'hide_tip': None,
            'input_boxes': None, 'input_size': None, 'label_input_columns': None, 'location_city': None, 'location_country': None,
            'location_defaultcoordinates': None, 'location_mapheight': None, 'location_mapservice': None, 'location_mapwidth': None,
            'location_mapzoom': None, 'location_nodefaultfromip': None, 'location_postal': None, 'location_state': None,
            'max_answers': None, 'max_filesize': None, 'max_num_of_files': None, 'max_num_value': None, 'max_num_value_n': None,
            'max_subquestions': None, 'maximum_chars': None, 'min_answers': None, 'min_num_of_files': None, 'min_num_value': None,
            'min_num_value_n': None, 'multiflexible_checkbox': None, 'multiflexible_max': None, 'multiflexible_min': None,
            'multiflexible_step': None, 'num_value_int_only': None, 'numbers_only': None, 'other_comment_mandatory': None,
            'other_numbers_only': None, 'other_position': None, 'other_position_code': None, 'other_replace_text': None,
            'page_break': None, 'parent_order': None, 'placeholder': None, 'prefix': None, 'printable_help': None,
            'public_statistics': None, 'random_group': None, 'random_order': None, 'rank_title': None, 'repeat_headings': None,
            'reverse': None, 'samechoiceheight': None, 'samelistheight': None, 'save_as_default': None, 'scale_export': None,
            'show_comment': None, 'show_grand_total': None, 'show_title': None, 'show_totals': None, 'showpopups': None,
            'slider_accuracy': None, 'slider_custom_handle': None, 'slider_default': None, 'slider_default_set': None,
            'slider_handle': None, 'slider_layout': None, 'slider_max': None, 'slider_middlestart': None, 'slider_min': None,
            'slider_orientation': None, 'slider_rating': None, 'slider_reset': None, 'slider_reversed': None, 'slider_separator': None,
            'slider_showminmax': None, 'statistics_graphtype': None, 'statistics_showgraph': None, 'statistics_showmap': None,
            'suffix': None, 'text_input_columns': None, 'text_input_width': None, 'time_limit': None, 'time_limit_action': None,
            'time_limit_countdown_message': None, 'time_limit_disable_next': None, 'time_limit_disable_prev': None,
            'time_limit_message': None, 'time_limit_message_delay': None, 'time_limit_message_style': None, 'time_limit_timer_style': None,
            'time_limit_warning': None, 'time_limit_warning_2': None, 'time_limit_warning_2_display_time': None,
            'time_limit_warning_2_message': None, 'time_limit_warning_2_style': None, 'time_limit_warning_display_time': None,
            'time_limit_warning_message': None, 'time_limit_warning_style': None, 'use_dropdown': None, 'value_range_allows_missing': None
        }

        # Update attributes with the provided object's attributes
        for attr in self.attributes:
            if hasattr(obj, attr) and attr == 'help':
                value = getattr( obj, 'help')
                if isinstance( value, str) and self.isHTML( value ):
                    value = self.cleanHTML( value )

                self.attributes[ attr ] = value

            elif hasattr( obj, attr ) and attr != 'help':
                self.attributes[attr] = getattr(obj, attr)
            else:
                print( f"{attr}")
                match attr:
                    case 'encrypted':
                        self.attributes[attr] = getattr(obj, "_encrypted") if hasattr( obj, "_encrypted" ) else None

                    case 'class':
                        self.attributes[attr] = getattr(obj, "_class")

                    case 'name':
                        self.attributes[attr] = getattr(obj, "title") if ( hasattr( obj, "title" ) and (getattr(obj, "_class") != 'G')) else getattr(obj, "group_name")

                    case 'text':
                        if getattr( obj, "_class" ) != "G":
                            value = getattr( obj, "question" )
                        else:
                            value = getattr( obj, "description")
                        if isinstance( value, str) and self.isHTML( value ):
                            value = self.cleanHTML( value )
                        self.attributes[attr] = value

                    case 'relevance':
                        if getattr( obj, "_class") == "G":
                            self.attributes[attr] = getattr(obj, "grelevance")

                    case 'type/scale':
                        self.attributes[attr] = getattr(obj, "_type") if (hasattr( obj, "_type" ) and (getattr(obj, "_class") != 'G')) else getattr(obj, "group_order")
                    case 'id':
                        self.attributes[attr] = getattr(obj, "qid") if getattr(obj, "_class") != 'G' else getattr(obj, "gid")

    #Search HTML tags
    def isHTML( self, string ):
        return bool( re.search (r'<[^>]+>', string) )

    def cleanHTML( self, html ):
        return html.replace('\t', '').replace('\n', '').strip()


    def __str__(self):
        # Convert all attributes to strings and filter out None values
        attributes_str = [str(self.attributes[attr]) if self.attributes[attr] is not None else "" for attr in self.attributes]

        # Join all attributes with tabs
        return "\t".join(attributes_str)