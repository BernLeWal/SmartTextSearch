#!/bin/python
from haystack.utils import convert_files_to_docs
from haystack.nodes import PreProcessor


## read and convert documents to store
dataset_dir = "./dataset"
all_docs = convert_files_to_docs(dir_path=dataset_dir)

preprocessor = PreProcessor(
    split_by="word",
    split_length=100,
    split_overlap=10,
    split_respect_sentence_boundary=True,
)

docs = preprocessor.process(all_docs)

print(f"n_files_input: {len(all_docs)}\nn_docs_output: {len(docs)}")

## add documents to store
from haystack.document_stores import InMemoryDocumentStore

document_store = InMemoryDocumentStore()
document_store.write_documents(docs)


## build DPR
from haystack.nodes import DensePassageRetriever

retriever = DensePassageRetriever(document_store,
                query_embedding_model="deepset/gbert-base-germandpr-question_encoder",
                passage_embedding_model="deepset/gbert-base-germandpr-ctx_encoder",
                embed_title=False)

document_store.update_embeddings(retriever)


## create Reader
from haystack.nodes import FARMReader

reader = FARMReader(model_name_or_path="deepset/gelectra-base-germanquad", use_gpu=True)

## initialize Pipeline
from haystack.pipelines import ExtractiveQAPipeline

pipeline = ExtractiveQAPipeline(reader, retriever)

## execute pipeline
prediction = pipeline.run(
    query="Wer ist in der Kommission bei kommissionellen Prüfungen?",
    params={
        "Retriever": {"top_k": 10},
        "Reader": {"top_k": 5}
    }
)


## print answers
from haystack.utils import print_answers

print_answers(
    prediction,
    details="minimum"   ## `minimum`, `medium` oder `all`
)
