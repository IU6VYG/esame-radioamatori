import React from 'react';
import Layout from '@theme-original/DocItem/Layout';
import type LayoutType from '@theme/DocItem/Layout';
import type {WrapperProps} from '@docusaurus/types';
import Admonition from '@theme/Admonition';

type Props = WrapperProps<typeof LayoutType>;

/**
 * Wrapper del layout delle pagine docs che aggiunge un disclaimer
 * informativo in cima a ogni pagina del sito.
 */
export default function LayoutWrapper(props: Props): React.JSX.Element {
  return (
    <>
      <Admonition type="warning" title="Nota importante">
        <p>
          Questi sono <strong>appunti personali</strong> e possono contenere errori o imprecisioni.
          Non sostituiscono libri di testo o fonti ufficiali. Il materiale è soggetto a revisione
          continua grazie al contributo volontario della comunità.{' '}
          <a href="https://github.com/IU6VYG/esame-radioamatori" target="_blank" rel="noopener noreferrer">
            Contribuisci su GitHub
          </a>.
        </p>
      </Admonition>
      <Layout {...props} />
    </>
  );
}
